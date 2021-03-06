from ..selectors import strip_relay_selectors


def test_strip_relay_selectors():
    selector = {
        'edges': {
            'node': {
                'id': None,
            }
        }
    }
    stripped_selector = strip_relay_selectors(selector)
    assert stripped_selector == {
        'id': None,
    }


def test_complex_strip_relay_selectors():
    selector = {
        'pizzas': {
            'edges': {
                'node': {
                    'id': None,
                    'fields': {
                        'id': None,
                        'relay_fields': {
                            'edges': {
                                'node': {
                                    'id': None,
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    stripped_selector = strip_relay_selectors(selector)
    assert stripped_selector == {
        'pizzas': {
            'id': None,
            'fields': {
                'id': None,
                'relay_fields': {
                    'id': None,
                }
            }
        }
    }
