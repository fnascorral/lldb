from __future__ import print_function

import unittest2

from lldbsuite.test.decorators import *
from lldbsuite.test.concurrent_base import ConcurrentEventsBase
from lldbsuite.test.lldbtest import TestBase


@skipIfWindows
class ConcurrentSignalNWatchNBreak(ConcurrentEventsBase):

    mydir = ConcurrentEventsBase.compute_mydir(__file__)

    @skipIfFreeBSD # timing out on buildbot
    @skipIfRemoteDueToDeadlock
    @expectedFailureAll(triple = '^mips') # Atomic sequences are not supported yet for MIPS in LLDB.
    def test_signal_n_watch_n_break(self):
        """Test one signal thread with 5 watchpoint and breakpoint threads."""
        self.build(dictionary=self.getBuildFlags())
        self.do_thread_actions(num_signal_threads=1,
                               num_watchpoint_threads=5,
                               num_breakpoint_threads=5)


