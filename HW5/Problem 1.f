
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
      subroutine accel(np,x,y,z,ax,ay,az,sx,sy,sz,pot)
!                compute the acceleration and potential energy
      real*8 x(128),y(128),z(128),ax(128),ay(128),az(128)
      real*8 dx,dy,dz,adx,ady,adz
      real*8 ri,ri2,ri4,ri6,ri8,b,sx,sy,sz
!----------------------- initialize acceleration vector
      do i=1,np 
      ax(i)=0.d0
      ay(i)=0.d0
      az(i)=0.d0
      end do
      pot=0.d0
!----------------------- compute pair-wise force
      do i=1,(np-1)
        do j=i+1,np
          dx=x(i)-x(j)
          dy=y(i)-y(j)
!          dz=z(i)-z(j)
!-----------------minimun image distance
          adx=dabs(dx)
          ady=dabs(dy)
!          adz=dabs(dz)
          if(adx.gt.0.5*sx) dx=dx-dsign(sx,dx)
          if(ady.gt.0.5*sy) dy=dy-dsign(sy,dy)
!          if(adz.gt.0.5*sz) dz=dz-dsign(sz,dz)
!         ri2=1.d0/(dx*dx+dy*dy+dz*dz)
          ri2=1.d0/(dx*dx+dy*dy)
          ri4=ri2*ri2
          ri6=ri4*ri2
          ri8=ri6*ri2
          pot=pot+(ri6-1.d0)*ri6
          b=24.d0*(2.d0*ri6-1.)*ri8
          ax(i)=ax(i)+b*dx
          ay(i)=ay(i)+b*dy
!          az(i)=az(i)+b*dz
          ax(j)=ax(j)-b*dx
          ay(j)=ay(j)-b*dy
!          az(j)=az(j)-b*dz
        end do
      end do
      pot=4.0*pot
      return
      end
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      subroutine update(np,x,y,z,vx,vy,vz,ax,ay,az,sx,sy,sz,dt,pot,ek)
      real*8 x(128),y(128),z(128)
      real*8 vx(128),vy(128),vz(128)
      real*8 ax(128),ay(128),az(128)
      real*8 dt,hdt2,hdt,sx,sy,sz
!
      ek=0.d0
      hdt=0.5d0*dt
      hdt2=hdt*dt
           do i=1,np
           vx(i)=vx(i)+hdt*ax(i)
           vy(i)=vy(i)+hdt*ay(i)
!          vz(i)=vz(i)+hdt*az(i)
!
           x(i)=x(i)+dt*vx(i)
           y(i)=y(i)+dt*vy(i)
!          z(i)=z(i)+dt*vz(i)
           end do
           call accel(np,x,y,z,ax,ay,az,sx,sy,sz,pot)
!--------------------------- enforce pbc-------
           do i=1,np
           x(i)=dmod(x(i)+sx,sx)
           y(i)=dmod(y(i)+sy,sy)
!          z(i)=dmod(z(i)+sz,sz)
           vx(i)=vx(i)+hdt*ax(i)
           vy(i)=vy(i)+hdt*ay(i)
!          vz(i)=vz(i)+hdt*az(i)
           ek=ek+(vx(i)**2+vy(i)**2)
           end do
       ek=0.5d0*ek
       return
       end
    