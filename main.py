import pandas as pd

def read_links_from_file(filepath):
    """Reads links from a text file, assuming one link per line."""
    with open(filepath, 'r', encoding='utf-8') as f:
        # Strip whitespace and ignore empty lines
        return [line.strip() for line in f if line.strip()]

def segregate_links(liked_links, all_links):
    """
    Segregates links into liked and disliked.
    """
    # Maintain a set of liked links for fast O(1) lookup
    liked_set = set(liked_links)
    
    # Filter all_links to find the ones we don't like
    # This preserves the order of links as they appear in all_links
    disliked_links = [link for link in all_links if link not in liked_set]
    
    return liked_links, disliked_links

def main():
    # --- OPTION 1: Read from text files (Recommended for large lists) ---
    # To use this, create 'liked_links.txt' and 'all_links.txt' in the same folder, 
    # paste your links in them (one link per line), and uncomment the two lines below:
    
    liked_links = read_links_from_file('liked_links.txt')
    all_links = read_links_from_file('all_links.txt')
    
    # --- OPTION 2: Hardcoded links (Useful for testing) ---
    # For demonstration, we'll use these hardcoded lists. 
    # You can replace these with your actual links if you prefer not to use files.
    # liked_links = [
    #     "https://example.com/liked1",
    #     "https://example.com/liked2",
    #     "https://example.com/liked3"
    # ]
    
    # all_links = [
    #     "https://example.com/disliked1",
    #     "https://example.com/liked2",
    #     "https://example.com/liked1",
    #     "https://example.com/disliked2",
    #     "https://example.com/liked3",
    #     "https://example.com/disliked3"
    # ]
    
    print(f"Loaded {len(liked_links)} liked links and {len(all_links)} total links.")
    
    # Process the links
    liked, disliked = segregate_links(liked_links, all_links)
    
    print(f"Found {len(disliked)} disliked links.")
    
    # Create pandas DataFrames to hold the data
    df_liked = pd.DataFrame(liked, columns=["Liked Links"])
    df_disliked = pd.DataFrame(disliked, columns=["Disliked Links"])
    
    # Save the DataFrames to Excel files
    # Setting index=False prevents pandas from writing row numbers to the Excel file
    try:
        df_liked.to_excel("liked_links.xlsx", index=False)
        df_disliked.to_excel("disliked_links.xlsx", index=False)
        print("Successfully segregated links into 'liked_links.xlsx' and 'disliked_links.xlsx'.")
    except Exception as e:
        print(f"An error occurred while saving to Excel: {e}")
        print("Please make sure you have 'openpyxl' installed (run 'pip install openpyxl' in the terminal).")

if __name__ == "__main__":
    main()
