.PHONY: all

HOME_FILES=$(addprefix ./home/, $(shell ls -A ./home/))

all:
	cp -rf $(HOME_FILES) ~