# Learn Python in 100 days

## Tips

### Print with format
```python
name = 'Supachai'
msg = f'Hello {name}'
```

### Short-if
```python
x = 0 if x < 1 else x 
```

### Play with String
```python

# lower case
"message".lower()

# count "a" in string
"how many a in strin".count('a')
```

### Get value list from dict
```python
dict.values()
```

### Sum number in list
```python
sum([1, 2, 3])
```

### pip
```bash
# Install Virtual env
apt-get install python3-venv

# Create venv
python3 -m venv myenv

# Active emv
source ./venv/bin/activate

# Check package and update
pip3 list
pip3 install --upgrade pip
pip3 install --upgrade setuptools
```