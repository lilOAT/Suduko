from test_grid_utils import *

def main():
    print("Executing Test Harness...")
    print("---------------------------")
    print()
    print("Testing grid_utils...")
    print("    Testing import_grid...")
    print("        ",test_import_grid())
    print("    Testing export_grid...")
    print("        ",test_export_grid())
    print("    Testing initialise_candidate_grid...")
    print("        ",test_initialise_candidate_grid())
    print("    Testing is_number_in_block...")
    print("        ",test_is_number_in_block())
    print("    Testing is_number_in_row...")
    print("        ",test_is_number_in_row())
    print()




if __name__ == '__main__':
    main()