" All system-wide defaults are set in $VIMRUNTIME/debian.vim and sourced by
" the call to :runtime you can find below.  If you wish to change any of those
" settings, you should do it in this file (/etc/vim/vimrc), since debian.vim
" will be overwritten everytime an upgrade of the vim packages is performed.
" It is recommended to make changes after sourcing debian.vim since it alters
" the value of the 'compatible' option.

runtime! debian.vim

" Vim will load $VIMRUNTIME/defaults.vim if the user does not have a vimrc.
" This happens after /etc/vim/vimrc(.local) are loaded, so it will override
" any settings in these files.
" If you don't want that to happen, uncomment the below line to prevent
" defaults.vim from being loaded.
" let g:skip_defaults_vim = 1

" Uncomment the next line to make Vim more Vi-compatible
" NOTE: debian.vim sets 'nocompatible'.  Setting 'compatible' changes numerous
" options, so any other options should be set AFTER setting 'compatible'.
"set compatible

" Vim5 and later versions support syntax highlighting. Uncommenting the next
" line enables syntax highlighting by default.
if has("syntax")
  syntax on
endif

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
set background=dark

" Uncomment the following to have Vim jump to the last position when
" reopening a file
"au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" Uncomment the following to have Vim load indentation rules and plugins
" according to the detected filetype.
"filetype plugin indent on
filetype plugin on

let mapleader = ":"

"Common
:inoremap <Leader>S <Esc>:w<CR>
:nnoremap <Leader>S <Esc>:w<CR>
:inoremap ( ()<Esc>i
:inoremap [ []<Esc>i
:inoremap { {}<Esc>i
:inoremap " ""<Esc>i
:inoremap ' ''<Esc>i
:inoremap <Leader>< <Esc>i
:nnoremap <Leader>< hi
:inoremap <Leader>> <Esc>la
:nnoremap <Leader>> <Esc>la
:inoremap <Leader><Space> <Esc>/<++><CR>cf>
:nnoremap <Leader><Space> <Esc>/<++><CR>cf>
:inoremap <Leader>o <Esc>o
:inoremap <Leader>O <Esc>O
:inoremap <Leader>A <Esc>A
:inoremap <Leader>I <Esc>I
:inoremap <Leader>D <Esc>S
:nnoremap <Leader>C <Esc>gg"+yG
:inoremap <Leader>C <Esc>gg"+yG

"Python
autocmd Filetype python inoremap :: <Esc>A:
autocmd Filetype python nnoremap :: <Esc>A:
autocmd Filetype python inoremap <Leader>F def (<++>):<Esc>bi
autocmd Filetype python inoremap <Leader>M if __name__ == "__main__":<Esc>o
autocmd BufEnter *.pyx :setlocal filetype=python
"autocmd Filetype python setlocal noexpandtab shiftwidth=8

"SQL
autocmd Filetype sql inoremap ;; <Esc>A;
autocmd Filetype sql nnoremap ;; <Esc>A;<Esc>

"Languages
map <F4> :set spelllang=en<CR>
map <F3> :set spelllang=es<CR>

" The following are commented out as they cause vim to behave a lot
" differently from regular Vi. They are highly recommended though.
"set showcmd		" Show (partial) command in status line.
"set showmatch		" Show matching brackets.
"set ignorecase		" Do case insensitive matching
"set smartcase		" Do smart case matching
"set incsearch		" Incremental search
"set autowrite		" Automatically save before commands like :next and :make
"set hidden		" Hide buffers when they are abandoned
"set mouse=a		" Enable mouse usage (all modes)

set number
set relativenumber
"set tabstop=8
"set shiftwidth=8
"set noexpandtab
colorscheme delek

if &diff
	colorscheme elflord
endif

" Source a global configuration file if available
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif

