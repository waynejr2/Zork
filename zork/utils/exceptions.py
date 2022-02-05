class NoConfigurationFileFound(Exception):
    """ Triggered when the program it's launched and no 'CPY++' config file 
        is located """
    def __init__(self, message:str='No cpy++.conf file found'):
        self.message = message
        super().__init__(self.message)

class DuplicatedAttribute(Exception):
    """ If an attribute it's found by duplicated on the config file """
    def __init__(self, attr_name: str):
        super().__init__(f'{attr_name} is already defined in the file')

class MissedMandatoryAttributes(Exception):
    """ A mandatory attribute it's not defined in the configuration file """
    def __init__(self, missed_attrs: list):
        attr_str = 'Attribute: ' if len(missed_attrs) == 1 else 'Attributes: '
        is_are = "is" if len(missed_attrs) == 1 else "are"
        isnt_arent = "isn't" if len(missed_attrs) == 1 else "aren't"
        super().__init__(
            f'\n\t{attr_str + ", " .join(map(str, missed_attrs))}, which {is_are} mandatory, {isnt_arent} present in the config file'
        )

class UnknownAttribute(Exception):
    """ Not defined or available attribute found """
    def __init__(self, attr_name: str):
        super().__init__(f'{attr_name} is an unknown or unsupported attribute')

class UnknownProperty(Exception):
    """ Not defined or available attribute found " """
    def __init__(self, property_name: str):
        super().__init__(f'{property_name} is an unknown or unsupported property')

class ErrorFileFormat(Exception):
    """ Not defined or available attribute found " """
    def __init__(self, idx, error):
        super().__init__(
            f'ERROR in line: {idx}: \n\t{error}\n' + 
            'Not valid sentence or format error'
        )