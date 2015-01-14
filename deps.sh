#!/usr/bin/env bash
# Installs the packages in PIP_PACKAGES using pip and the U_PACKAGES using apt
# Nicolas Valcarcel <nvalcarcel@gmail.com>

B_DEPS=''

PIP_PACKAGES=''
PIP_FREEZE=''
U_PACKAGES=''


if [[ -n "${B_DEPS}" ]]; then
    sudo apt-get build-dep $B_DEPS
fi

if [[ -n "${U_PACKAGES}" ]]; then
    sudo apt-get install $U_PACKAGES
fi

dpkg-architecture -iamd64

if [[ $? -eq 0 ]] && [[ "${U_PACKAGES}" == *libjpeg-dev* ]]; then
    if [[ ! -f /usr/lib/libjpeg.so ]]; then
        sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
    fi
    if [[ ! -f /usr/lib/libfreetype.so ]]; then
        sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
    fi
    if [[ ! -f /usr/lib/libz.so ]]; then
        sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
    fi
fi

if [[ -n "${PIP_PACKAGES}" ]]; then
    for package in $PIP_PACKAGES
    do
        pip install $package
    done
fi

if [[ -n "${PIP_FREEZE}" ]]; then
    pip install -r $PIP_FREEZE
fi
