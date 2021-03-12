git filter-branch -f --env-filter "GIT_AUTHOR_NAME='Last-Vega'; GIT_AUTHOR_EMAIL='watanabe.shingo.ss@alumni.tsukuba.ac.jp'; GIT_COMMITTER_NAME='Last-Vega'; GIT_COMMITTER_EMAIL='watanabe.shingo.ss@alumni.tsukuba.ac.jp';" HEAD

git push -f origin master
