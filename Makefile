.PHONY:  test
test:
	pytest

.PHONY: uninstall_packages
uninstall_packages:
	@echo 'Removing all pip installed packages'
	pip freeze | xargs pip uninstall -y

.PHONY: install_packages
install_packages:
	@echo 'Installing all packages from requirements.txt'
	pip install -r requirements.txt

.PHONY: upgrade_pip
upgrade_pip:
	@echo 'Upgrading pip'
	pip install --upgrade pip
