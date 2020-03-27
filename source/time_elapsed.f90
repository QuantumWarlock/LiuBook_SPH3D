      subroutine time_elapsed(s)

!===============================================================================
!   The gfortran system time call is used to calculate the elapsed CPU
!===============================================================================

      implicit none

      real(8) :: s
      real(8) :: rCnt, rCntR
      integer(8) :: cnt, cntR, cntM

      call system_clock(cnt,cntR,cntM)
      rCnt = real(cnt,8)
      rCntR = real(cntR,8)
      s = rCnt/rCntR

      end subroutine time_elapsed
