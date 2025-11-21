# script to create and use a python environment for jupyter notebook launch
# source this file to run
#
# 1. create python environment
# 2. install missing packages
# 3. activte environment
# 4. run jupyter notebook
# 5. deactivate environment
#

command -v module >/dev/null 2>&1
if [ $? -eq 0 ]; then
  module purge
  module load python
fi

command -v python3 >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "***ERROR*** python3 environment not available!"
  echo "Try to install it on you system (on Ubuntu/Debian use \"sudo apt install python3-venv\" command)"
  return 1
fi

PYENVDIR=$HOME/pythonenv/python_intro
REPODIR=$(dirname $(readlink -f $BASH_SOURCE) )

if [ ! -f $PYENVDIR/bin/activate ]; then
  command -v python3 -m venv -h >/dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo "***ERROR*** python virtual environment module not available!"
    echo "Try to install it on you system (on Ubuntu/Debian use \"sudo apt install python3-venv\" command)"
    return 1
  fi
  echo -e "Python environment will be installed in:\n$PYENVDIR\n"
  echo -e "creating environment ... "
  python3 -m venv $PYENVDIR
  if [ $? -ne 0 ]; then
    echo "***ERROR*** cannot create python environment!"
    return 1
  fi
  echo -e "done!"
fi

activate () {
   if [ -z "$VIRTUAL_ENV" ]; then
     echo -e "activating environment from:\n$PYENVDIR\n"
     source $PYENVDIR/bin/activate
   fi

   if [ $? -ne 0 ]; then
      echo
      echo "***ERROR*** source this file"
      echo "source $BASH_SOURCE"
      echo
      return 2
   fi
}
activate

command -v jupyter >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "installing missing packages ..."
  pip install -r $REPODIR/requirements.txt
  if [ $? -ne 0 ]; then
      echo "***ERROR*** jupyter installation failed"
      return 3
  fi
fi

echo
echo "starting notebook ..."
echo -e "Jupyter notebook will be loaded from:\n$REPODIR\n"
jupyter notebook --no-browser --notebook-dir $REPODIR

echo "deactivating environment"
deactivate

echo "well done!"
