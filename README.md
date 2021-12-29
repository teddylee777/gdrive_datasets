### Installation

```python
!pip install gdrive_dataset
```
### Retrive `file_id`

for example: 

if `https://drive.google.com/file/d/abcdefgABCDEFG1234567/view` is a target google drive url, then

**abcdefgABCDEFG1234567** will be my **file_id**

```python
from gdrivedataset import loader

file_id = # put your file_id here
loader.load_from_google_drive(file_id)
```
