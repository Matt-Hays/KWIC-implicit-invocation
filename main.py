from KWICApp import KWICApp

if __name__ == "__main__":
    kwic = KWICApp()
    kwic.add_line("The quick brown fox")
    kwic.add_line("Jumped over the lazy dog")
    
    # search_term = "fox"
    # hits = kwic.find(search_term)
    # print(f"\nQUERY '{search_term} -> {hits}")
