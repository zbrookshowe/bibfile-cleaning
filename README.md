# BibTeX file cleaning for use in Overleaf documents
You go to generate a .bib file using a Zotero collection. After putting it into Overleaf, you get an error that can only be fixed by removing the "language" field. Furthermore, your bib file is plagued by bloat with papers with tons of authors and abstracts that you don't need, and you can't find a way to cut down on all that. Lastly, the paths on your computer to PDFs of the papers you're citing are included and you don't want your computer's file path info in your Overleaf folder. If you've faced any of these issues, look no further!

This small program will remove any of the following fields from the Zotero-generated BibTeX fields automatically:
- language
- file
- abstract (including multi-line abstracts)

and will trim down the list of authors to the number you want, using the entry "others" which results in BibTeX printing *et al.* in the bibliography.
