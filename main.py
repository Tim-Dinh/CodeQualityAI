import multiprocessing
import pandas as pd
from config import NUM_WORKERS
from file_selector import get_selected_files
from analyzer import analyze_file

def main():
    """Main execution function for analyzing files."""
    file_paths = get_selected_files()
    if not file_paths:
        print("No files selected for analysis.")
        return

    print(f"Total files to process: {len(file_paths)}")

    with multiprocessing.Pool(NUM_WORKERS) as pool:
        results = pool.map(analyze_file, file_paths)

    # Convert results into DataFrame
    columns = ["Filename", "Duplication Summary", "Duplication Advice", "Duplication Score",
               "Unit Size Summary", "Unit Size Advice", "Unit Size Score",
               "Complexity Summary", "Complexity Advice", "Complexity Score",
               "Unit Interfacing Summary", "Unit Interfacing Advice", "Unit Interfacing Score",
               "Coupling Summary", "Coupling Advice", "Coupling Score",
               "Coding Standards Summary", "Coding Standards Advice", "Coding Standards Score"]
    
    df = pd.DataFrame(results, columns=columns)

    # Save results to Excel
    excel_file = "code_analysis.xlsx"
    df.to_excel(excel_file, index=False)
    print(f"\nAnalysis complete! Results saved in '{excel_file}'")

if __name__ == "__main__":
    main()
