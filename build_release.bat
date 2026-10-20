@echo off
rem Builds the book's itch.io downloads into dist\: game-design-technology.zip (the offline HTML edition)
rem and game-design-technology.epub. To redo the promo images and the EPUB cover too, run
rem python tools\book_promo.py instead (it runs this same build as well).
cd /d "%~dp0"
python tools\book.py release || (pause & exit /b 1)
explorer dist
