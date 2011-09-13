all: apd_sandbox.php ana.py

apd_sandbox.php: apd_generate.py
	python apd_generate.py > apd_sandbox.php

ana.py: generate-ana.py
	python generate-ana.py > ana.py
