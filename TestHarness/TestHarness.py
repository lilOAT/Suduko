from test_grid_utils import *
from test_grid_operations import *
from test_solving_techniques import *

def main():
    print("Executing Test Harness...")
    print("---------------------------")
    print()
    print("Testing grid_utils...")
    print("    import_grid...")
    print("        ",test_import_grid())
    print("    export_grid...")
    print("        ",test_export_grid())
    print("    initialise_candidate_grid...")
    print("        ",test_initialise_candidate_grid())
    print("    is_number_in_block...")
    print("        ",test_is_number_in_block())
    print("    is_number_in_row...")
    print("        ",test_is_number_in_row())
    print()
    print("Testing grid_operations...")
    print("    solve_cell...")
    print("        ",test_solve_cell())
    print("    update_candidate_row...")
    print("        ",test_update_candidate_row())
    print("    update_candidate_col...")
    print("        ",test_update_candidate_col())
    print("    update_candidate_block...")
    print("        ",test_update_candidate_block())
    print()
    print("Testing solving_techniques...")
    print("    naked_single_check...")
    print("        ",test_naked_single_check())
    print("    hidden_single_row_check...")
    print("        ",test_hidden_single_row_check())
    print("    hidden_single_col_check...")
    print("        ",test_hidden_single_col_check())
    print("    hidden_single_block_check...")
    print("        ",test_hidden_single_block_check())

    print()




if __name__ == '__main__':
    main()