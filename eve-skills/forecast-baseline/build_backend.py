"""Original minimal PEP 517 wheel backend. Standard library only."""
import base64
import csv
import hashlib
import io
from pathlib import Path
import zipfile

NAME = 'forecast-baseline'
MODULE = 'local_forecast_baseline'
VERSION = '0.1.0'


def get_requires_for_build_wheel(config_settings=None):
    return []


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    root=Path(__file__).resolve().parent
    dist=NAME.replace('-','_')
    info=f'{dist}-{VERSION}.dist-info'
    files={p.relative_to(root/'src').as_posix():p.read_bytes() for p in sorted((root/'src').rglob('*.py'))}
    metadata=f'Metadata-Version: 2.1\nName: {NAME}\nVersion: {VERSION}\nSummary: Offline analytical skill with CLI and legacy MCP stdio\nLicense: MIT\nRequires-Python: >=3.10\n\nOriginal generated implementation; no third-party runtime dependencies.\n'
    files[info+'/METADATA']=metadata.encode()
    files[info+'/WHEEL']=b'Wheel-Version: 1.0\nGenerator: original-stdlib-backend\nRoot-Is-Purelib: true\nTag: py3-none-any\n'
    files[info+'/entry_points.txt']=f'[console_scripts]\n{NAME} = {MODULE}.runtime:main\n'.encode()
    for name in ('LICENSE','NOTICE'):
        files[info+'/'+name]=(root/name).read_bytes()
    record=io.StringIO(newline=''); writer=csv.writer(record,lineterminator='\n')
    for path,data in sorted(files.items()):
        digest=base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b'=').decode()
        writer.writerow((path,'sha256='+digest,len(data)))
    writer.writerow((info+'/RECORD','','')); files[info+'/RECORD']=record.getvalue().encode()
    filename=f'{dist}-{VERSION}-py3-none-any.whl'
    target=Path(wheel_directory); target.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(target/filename,'w',compression=zipfile.ZIP_STORED) as z:
        for path,data in sorted(files.items()):
            zi=zipfile.ZipInfo(path,date_time=(2020,1,1,0,0,0)); zi.external_attr=0o100644 << 16
            z.writestr(zi,data)
    return filename
