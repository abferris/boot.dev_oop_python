
set -e

export PYTHONPATH=$(pwd)

python3 -m unittest discover -s src/tests -p "test_*.py"