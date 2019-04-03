# coders_forum
A repo to document the tutorials/rants/discussions/musings at the coder's forum

Links: [Scratchpad](https://docs.google.com/document/d/1ocrq-v7jm3exNSgxgpJxXSx83Q-QR6L1faBA0ciPJ8I/edit?usp=sharing), [Topics](https://docs.google.com/document/d/13q61Xj0J1JbFwYZAcjiyVnDRAkrHkjgttJwFmsaATTI/edit?usp=sharing)


To contribute:

1. Run a notebook server locally and fill a notebook with wisdom.

2. Clone this directory locally and change your working directory to it:

  ```
  git clone https://github.com/nih-fmrif/coders_forum.git
  cd coders_forum
  ```

3. If the target directory does not exist in the repository make it (notebooks should be placed in a directory by the name YYYY_MM):

  ```
  mkdir 2019_04
  ```

4. If you haven't already, install gitautopush:

  ```
  pip install gitautopush
  ```

5. Run gitautopush to sync your notebook to the repository. When finished, stop gitautopush. Remember to use the "--out-name" option of gitautopush:
  ```
  gitautopush path/to/local/notebook.ipynb --out-name 2019_04/demo_notebook.ipynb
  ```