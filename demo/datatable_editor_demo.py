#%% Simple demo for running Datatable editor

from datatable_editor.core import DatatableEditor

# Import example data
from demo_data.demo_data import display_tables_dict

# Initiated editor object
editor = DatatableEditor(datatables=display_tables_dict, port=8052, debug=True)

# Run the editor -> will run at localhost:<specified_port>
editor.run_app()
