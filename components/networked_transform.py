from io_hubs_addon.components.hubs_component import HubsComponent
from io_hubs_addon.components.types import NodeType, PanelType
from ..utils import do_register, do_unregister


class NetworkedTransform(HubsComponent):
    _definition = {
        'name': 'networked-transform',
        'display_name': 'Networked Transform',
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'EMPTY_AXIS',
        'deps': ['networked'],
        'version': (1, 0, 0)
    }


def register():
    do_register(NetworkedTransform)


def unregister():
    do_unregister(NetworkedTransform)
