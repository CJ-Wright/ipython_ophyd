import os

# expected code
# 0 -> beamline
# 1 -> test
# 2 -> simulation
os.environ['XPDAN_SETUP'] = str(0)

# setup glbl
from xpdan.glbl import an_glbl
from xpdan.pipelines.main import *
# from xpdan.pipelines.callback import MainCallback

an_glbl['exp_db'] = db  # alias
calibration_md_folder['file_path'] = os.path.join( an_glbl['config_base'],
                                                   'xpdAcq_calib_info.yml')
d.subscribe(lambda x: raw_source.emit(x))
