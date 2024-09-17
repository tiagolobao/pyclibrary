
import debugpy
import pytest

DEBUG_ON = False

@pytest.fixture(scope='session', autouse=True)
def setup_debugger():
    debugpy.listen(('0.0.0.0', 5678))
    if DEBUG_ON == True:
        print("Waiting for debugger to attach...")
        debugpy.wait_for_client()
        debugpy.breakpoint()