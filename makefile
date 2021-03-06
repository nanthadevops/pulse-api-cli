TARGET=boundary
VERSION=$(shell python -c "from boundary import __version__ ; print(__version__)")
TAR_FILE=dist/boundary-$(VERSION).tar.gz

install: build
	pip install $(TAR_FILE)

build:
	python setup.py sdist

doc:
	pandoc -f markdown -t plain README.md > README.txt

rebuild: clean install

upload:
	python setup.py sdist upload
	
clean:
	/bin/rm -rf build dist site MANIFEST
	pip freeze | grep "boundary==$(VERSION)" && pip uninstall -y $(TARGET)
