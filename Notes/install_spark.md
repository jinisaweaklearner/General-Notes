```
# use brew to install spark
brew install apache-spark

# check info of spark
brew info apache-spark

# touch a new file if it does not exist
touch ~/.bash_profile

# paste info into that file
export SPARK_PATH=(path found above by running brew info apache-spark)
export PYSPARK_DRIVER_PYTHON="jupyter" 
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
#For python 3, You have to add the line below or you will get an error#
export PYSPARK_PYTHON=python3
alias snotebook='$SPARK_PATH/bin/pyspark --master local[2]'

# install java 8
brew tap adoptopenjdk/openjdk
brew install --cask adoptopenjdk8
```
