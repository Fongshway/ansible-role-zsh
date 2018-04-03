import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zsh_package(host):
    assert host.package("zsh").is_installed


def test_antibody_is_installed(host):
    assert host.file("/usr/local/bin/antibody").exists


def test_zshrc_file(host):
    assert host.file("/home/user/.zshrc").exists


def test_anitbody_home(host):
    assert host.file("/home/user/.cache/antibody").exists
