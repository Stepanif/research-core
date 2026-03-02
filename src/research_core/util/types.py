class ResearchError(Exception):
    pass


class ContractError(ResearchError):
    pass


class ParseError(ResearchError):
    pass


class ValidationError(ResearchError):
    pass
