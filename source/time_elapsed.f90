      subroutine time_elapsed(s)

!===============================================================================
!   The standard Fortran 90 routine RTC is used to calculate the elapsed CPU
!===============================================================================

      implicit none

      integer, parameter :: output = 6
      real(8) :: s

      s = time()

      end subroutine time_elapsed
