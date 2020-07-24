! Homework 9 - PIMC Integration
! Problem 2
implicit none
real*8 x(2), xmax, dtau, tau, acc, accav
real*8 e, el(1000000), elav, stderr, anal
real*8 pi
integer n, i, j

open(unit = 16, file = 'acceptance.pl')
open(unit = 17, file = 'var.pl')
open(unit = 18, file = 'varfine.pl')
open(unit = 19, file = 'analvar.pl')


pi = 3.14159265359d0

call random_number(e)

n = 1000000

do j = 2, 20
  tau = 0.5d0 * j
  dtau = tau / 2
  accav = 0.d0
  e = 0.d0
  el = 0.d0
  xmax = 2.5d0
  call random_number(x)

  do i = 1, 2000
    call metro(x, xmax, acc, dtau)
  end do

  do i = 1, n

    call metro(x, xmax, acc, dtau)
    accav = accav + acc
    
    call getE(e, x(1), x(2), dtau)
    el(i) = el(i) + e / 2
    call getE(e, x(2), x(1), dtau)
    el(i) = el(i) + e / 2
    !write(*,*) el(i)

  end do
  
  accav = accav / n
  elav = sum(el) / n
  el(:) = el(:) - elav
  el = el**2
  stderr = dsqrt(sum(el) / (n - 1)) / dsqrt(dble(n))
  write(*,*) j
  write(16,*) tau, accav
  write(17,*) tau, elav, stderr
  call getReal(anal, tau)
  write(18,*) tau, elav - anal, stderr
  write(19,*) tau, anal
end do

!goto 69
!69 continue

end


!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

subroutine relpfun(relp, x1, x2, dtau, dx)
real*8 relp, x1, x2, dx(2), dtau
real*8 s12, s21

call getS(s12, x1, x2, dtau)
call getS(s21, x2, x1, dtau)
relp = 1 / exp(s12 + s21)

call getS(s12, x1 + dx(1), x2 + dx(2), dtau)
call getS(s21, x2 + dx(2), x1 + dx(1), dtau)
relp = 1 / exp(s12 + s21) / relp

return
end

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

subroutine metro(x, xmax, acc, dtau)
real*8 x(2), dx(2), xmax, relp, rng, acc, dtau


call random_number(dx)

dx = xmax * (dx - 0.5d0)
call relpfun(relp, x(1), x(2), dtau, dx)
call random_number(rng)
if (rng.lt.relp) then
  x = x + dx
  acc = 1.d0
else
  acc = 0.d0
end if

return
end



!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

subroutine getS(s, x, xp, dtau)
real*8 s, x, xp, dtau

s = 0.5d0 * log(2 * 3.1415926535898d0 * dtau) !!!!!!!!!!!!!!!!!!
s = s + (x - xp)**2 / 2 / dtau
s = s + dtau * (x**2 + xp**2) / 4

return
end

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

subroutine getE(e, x, xp, dtau)
real*8 e, x, xp, dtau

e = (1 / dtau + dtau / 2 - ((x - xp) / dtau + 0.5d0 * dtau * x)**2 + x**2) / 2

return
end

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

subroutine getReal(anal, tau)
real*8 anal, tau

anal = 0.5d0 + 1 / (exp(tau) - 1)

return
end
