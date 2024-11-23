from abcli.help.generic import help_functions as generic_help_functions

from blueflow import ALIAS
from blueflow.help.huggingface import help_functions as help_huggingface
from blueflow.help.workflow import help_functions as help_workflow

help_functions = generic_help_functions(plugin_name=ALIAS)


help_functions.update(
    {
        "huggingface": help_huggingface,
        "workflow": help_workflow,
    }
)
