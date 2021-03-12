git filter-branch -f --env-filter "GIT_AUTHOR_NAME='Last-Vega'; GIT_AUTHOR_EMAIL='watanabe.shingo.ss@alumni.tsukuba.ac.jp'; GIT_COMMITTER_NAME='Last-Vega'; GIT_COMMITTER_EMAIL='watanabe.shingo.ss@alumni.tsukuba.ac.jp';" -- --all

git push -f origin master

#!/bin/bash
git filter-branch -f --env-filter "
if [ ${GIT_AUTHOR_NAME}='Sydney' ]; then
  export GIT_AUTHOR_NAME='Last-Vega'
  export GIT_AUTHOR_EMAIL='watanabe.shingo.ss@alumni.tsukuba.ac.jp'
  export GIT_COMMITTER_NAME='Last-Vega'
  export GIT_COMMITTER_EMAIL='watanabe.shingo.ss@alumni.tsukuba.ac.jp'
fi
" -- --all