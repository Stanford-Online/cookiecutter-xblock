xblock_short_name=foobarxblock
xblock_long_name=FoobarXblock
test:
	pip install cookiecutter
	rm -rf $(xblock_short_name)/
	cookiecutter --no-input ./
	make -C $(xblock_short_name) test
