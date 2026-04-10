from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

my_north_tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-plugin-fitness.',
    image='ghcr.io/ebb2675/nomad-plugin-fitness:main',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-plugin-fitness.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'esma.boydas@physik.hu-berlin.de', 'name': 'Esma Boydas'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='my_north_tool',
)

north_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad-plugin-fitness-my-north-tool',
    north_tool=my_north_tool,
)
