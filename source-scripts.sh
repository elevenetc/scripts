#!/usr/bin/env bash

scriptsPath=${argv}
source ${scriptsPath}/android/and.sh
source ${scriptsPath}/git/git.sh
source ${scriptsPath}/net/net.sh
source ${scriptsPath}/utils/utils.sh
source ${scriptsPath}/pm2/pm2.sh
source ${scriptsPath}/osx/osx.sh
source ${scriptsPath}/fs/fs.sh
source ${scriptsPath}/mysql/mysql.sh
source ${scriptsPath}/ssh/ssh.sh
source ${scriptsPath}/messages/errors.sh
source ${scriptsPath}/messages/success.sh
source ${scriptsPath}/pm/pm.sh
source ${scriptsPath}/edit/edit.sh
source ${scriptsPath}/media/media.sh
source ${scriptsPath}/gradle/gradle.sh
source ${scriptsPath}/paths/paths.sh
source ${scriptsPath}/system/system.sh
source ${scriptsPath}/sims/sims.sh
source ${scriptsPath}/format/format.sh
source ${scriptsPath}/dev/dev.sh
source ${scriptsPath}/docker/docker.sh
source ${scriptsPath}/aws/aws.sh
source ${scriptsPath}/bamboo/bamboo.sh
source ${scriptsPath}/open/open.sh
source ${scriptsPath}/cd/cd.sh

source $HOME/.bash_profile

alias media-mov-to-mkv="python ${scriptsPath}/media/media-mov-to-mkv.py"
alias fs-find-and-rename="python ${scriptsPath}/fs/fs-find-and-rename.py"
alias android-multi-call="python ${scriptsPath}/android/adb-multi-call.py"
alias bookmarks="python ${scriptsPath}/bookmarks/bookmarks.py"
alias imagecat=${scriptsPath}/fs/imgcat.sh

# ZSH plugins
# zsh-autosuggestions: git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
# zsh-syntax-highlighting: git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
# ctrl+t search: git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf && ~/.fzf/install
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
)
