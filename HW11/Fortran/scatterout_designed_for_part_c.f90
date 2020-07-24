!/*
! * One dimensional scattering - transmission coefficents
! */
!----------------------------main program declarations
       implicit real*8 (a-h, o-z)
real*8 pi,e0,v0,alpha,xint,x0,delx,tmax,delx2,dx,dk,dt,anorm,varg
!       parameter (hbar=1.d0, hbar2=1.d0, amass = 1.d0)  
       parameter (pi = 3.141592653589793d0, Ndim=16384/2)
       double precision x(Ndim),psi2(Ndim),psi(Ndim),psia2(ndim),vpot(ndim)
       complex*16 im,ExpT(Ndim),ExpV(Ndim),psiA(Ndim)
!
       open (unit=13, file='win.pl')
       open (unit=14, file='wout.pl')
!-------------------------main program
       im = dcmplx(0.d0,1.d0)
	   m=12
	   e0=59.2d0
	   v0=48.2d0
!	   alpha=2.d0
	   alpha=1.0d0
	   xint=800.d0
	   x0=-100.d0
	   delx=25.d0
	   tmax=25.d0
	   iswitch=1
!

       N=2**m
       Nhalf = N/2
       delx2 = delx*delx        
!
!  Decide the grid sizes, and the time step in seconds.
!
       dx = xint/dble(N)
       dk = 2.d0*pi/xint
!  Save the x-grids and initialize the wavefunction:
!  x ranges from -N/2*dx to N/2*dx.
!
       Do i = 1, N
        x(i) = dx*(i-Nhalf)
       END DO
!

   do 200 iv=1,1
   dt=0.05+(iv-1)*.01d0
!       dt = 0.1              
       limit = int(tmax/dt+0.1)
!
     anorm = 1.d0/dsqrt(delx*dsqrt(2.d0*pi))
     ak0 = dsqrt(2.d0*E0)
       Do i = 1, N
        psiA(i) = anorm*cdexp(im*ak0*x(i)-(x(i)-x0)**2/(4.d0*delx2))
!        psiA(i)=psi(i)
       END DO
       y = pi*ak0/alpha      
       anum = (dsinh(y))**2
       ay0 = 8.d0*V0/(alpha*alpha)
       if (ay0.le.(1.d0)) then
        y0 = pi*dsqrt(1.d0 - ay0)/2.d0
        deno = 1.d0 + (dcos(y0))**2/anum
       else
        y0 = pi*dsqrt(ay0 - 1.d0)/2.d0
        deno = 1.d0 + (dcosh(y0))**2/anum
       end if
        TC = 1.d0/deno
!       write(14,46) TC
  46   format(/' theoretical transmission coefficient=', f10.6)
  99   format(16400(f10.6))
!  Initialize the arrays ExpT and ExpV,
! 
!  ExpT is an array of values exp(-i T(k) dt), where T(k)=E.
!
       DO i = 1, Nhalf
!   
! For k's between 0 and the Nyquist cutoff:
!
          ak  = dble(i-1) * dk
          E  = ak*ak/2.d0
          ExpT(i) = cdexp( -im * E * dt)
!
! K's above the Nyquist cutoff are actually negative:
!
          ak  = -dble(i) * dk
          E  = ak * ak / 2.d0 
          ExpT(N+1-i) = cdexp( -im * E * dt )
       END DO
!
!  ExpV is an array of values exp(-i V dt / 2)
!
       DO i = 1, N
	  varg=alpha*x(i)
	   If (dabs(varg).gt.100) then
	     v=0.0
	   else
           V = V0 / (dcosh(alpha*x(i)))**2
	   end if
	   vpot(i)=v
        ExpV(i) = cdexp( -im * V * dt / 2.d0 )
       END DO
!
!  Loop over propagation steps until time > MaxTime:
!
        evotime = 0.d0
       Do 100 j = 1, limit
!        evotime = evotime + dt
      call schem2A(m,N,ExpT,ExpV,psiA)       







!write to terminal, if iswitch = 0 will print result at all time steps, if iswitch = 1, only prints final result
 if(iswitch.eq.0) then
     if( mod(j,20).eq.0 ) then
       sumR=0.d0 
       sumT=0.d0 
       
       DO i = 1, Nhalf

        sumR = sumR + cdabs(psiA(i))**2
        sumT = sumT + cdabs(psiA(N+1-i))**2
		
		
	   end do
	   write(*,99) j*dt,dt,sumt/(sumt+sumr),tc, psiA
	   !write(14,99) j*dt,dt,sumt/(sumt+sumr),tc, psiA
     end if
 end if
 100   continue
   if( iswitch.eq.1 ) then
       sumR=0.d0 
       sumT=0.d0 
       DO i = 1, Nhalf
        sumR = sumR + cdabs(psiA(i))**2
        sumT = sumT + cdabs(psiA(N+1-i))**2
	   end do
!	   write(*,99) j*dt,dt,sumt/(sumt+sumr),(sumt+sumr)*dx
	   write(*,99) e0, sumt+sumr,sumt,tc
	   write(14,99) e0, sumt+sumr,sumt,tc
   end if
 200 continue
end











!-----------subprograms----------------------------------------------------
       Subroutine schem2A(m,N,ExpTA,ExpVA,psi)
! 
!   To calculate the 2nd-order decomposition scheme.
! 
       parameter (Ndim=16384/2)
       complex*16 ExpTA(1),ExpVA(1),psi(1),phi(Ndim)
!
        DO i = 1, N
          phi(i) = ExpVA(i) * psi(i)
        END DO
        call fft (phi, m, 0)
        DO i = 1, N
          phi(i) = ExpTA(i) * phi(i)
        END DO
        call fft (phi, m, 1 )
        DO i = 1, N
          psi(i) = ExpVA(i) * phi(i)
        END DO
!*
       return
       end 
!*


!*******************************************************************
!
      Subroutine FFT(A,m,INV)
!*------------------------------------------------------------------*
!*                                                                  *
!* A First Course in Computational Physics                          *
!*                                                                  *
!* Paul L. DeVries, Department of Physics, Miami University         *
!*                                                                  *
!* This subroutine performs the Fast Fourier Transform by           *
!* the method of Cooley and Tukey --- the FORTRAN code was          *
!* adapted from                                                     *
!*                                                                  *
!*   Cooley, Lewis, and Welch, IEEE Transactions E-12               *
!*       (March 1965).                                              *
!*                                                                  *
!* The array A contains the complex data to be transformed,         *
!* `m' is log2(N), and INV is an index = 1 if the inverse           *
!* transform is to be computed. (The forward transform is           *
!* evaluated if INV is not = 1.)                                    *
!*                                                                  *
!*                            start: 1965                           *
!*                    last modified: 1993                           *
!*                                                                  *
!------------------------------------------------------------------*
!*
       Complex*16 A(1), u, w, t
       Double precision ang, pi
       Integer N, Nd2, i, j, k, l, le, le1, ip
       Parameter (pi = 3.141592653589793d0)
!
!*  This routine computes the Fast Fourier Transform of the 
!*  input data and returns it in the same array. Note that 
!*  the k's and x's are related in the following way:
!*
!*    IF    K = range of k's      and     X = range of x's
!*
!*    THEN  delta-k = 2 pi / X    and   delta-x = 2 pi / K
!*        
!*  When the transform is evaluated, it is assumed that the 
!*  input data is periodic. The output is therefore periodic 
!*  (you have no choice in this). Thus, the transform is 
!*  periodic in k-space, with the first N/2 points being 
!*  'most significant'. The second N/2 points are the same 
!*  as the Fourier transform at negative k!!! That is,
!*
!*              FFT(N+1-i) = FFT(-i)  ,i = 1,2,....,N/2
!*
       N   = 2**m
       Nd2 = N/2
       j   = 1
       DO i = 1, N-1
          IF( i .lt. j ) THEN
             t    = A(j)
             A(j) = A(i)
             A(i) = t
          ENDIF
          k = Nd2
100       IF( k .lt. j ) THEN
             j = j-k
             k = k/2
             goto 100
          ENDIF
          j  = j+k
       END DO
       le = 1       
       DO l = 1, m
          le1 = le
          le  = le + le

          u = ( 1.D0, 0.D0 )
          ang = pi / dble(le1)
          W = Dcmplx( cos(ang), -sin(ang) )
          IF(inv .eq. 1) W = Dconjg(W)

          DO j = 1, le1
             DO i = j, N, le
                ip   = i+le1
                t    = A(ip)*u
                A(ip)= A(i)-t
                A(i) = A(i)+t
             END DO
             u=u*w
          END DO

       END DO

!c       IF(inv .ne. 1) THEN
       IF(inv .eq. 1) THEN
          DO i = 1, N
             A(i) = A(i) / dble(N)
          END DO
       ENDIF
	   return
       end
