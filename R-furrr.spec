#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-furrr
Version  : 0.1.0
Release  : 5
URL      : https://cran.r-project.org/src/contrib/furrr_0.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/furrr_0.1.0.tar.gz
Summary  : Apply Mapping Functions in Parallel using Futures
Group    : Development/Tools
License  : LGPL-2.1
Requires: R-future
Requires: R-globals
Requires: R-purrr
Requires: R-rlang
BuildRequires : R-future
BuildRequires : R-globals
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
[![Travis build
status](https://travis-ci.org/DavisVaughan/furrr.svg?branch=master)](https://travis-ci.org/DavisVaughan/furrr)
[![CRAN
status](https://www.r-pkg.org/badges/version/furrr)](https://cran.r-project.org/package=furrr)

%prep
%setup -q -c -n furrr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571834580

%install
export SOURCE_DATE_EPOCH=1571834580
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library furrr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library furrr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library furrr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc furrr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/furrr/DESCRIPTION
/usr/lib64/R/library/furrr/INDEX
/usr/lib64/R/library/furrr/Meta/Rd.rds
/usr/lib64/R/library/furrr/Meta/features.rds
/usr/lib64/R/library/furrr/Meta/hsearch.rds
/usr/lib64/R/library/furrr/Meta/links.rds
/usr/lib64/R/library/furrr/Meta/nsInfo.rds
/usr/lib64/R/library/furrr/Meta/package.rds
/usr/lib64/R/library/furrr/NAMESPACE
/usr/lib64/R/library/furrr/NEWS.md
/usr/lib64/R/library/furrr/R/furrr
/usr/lib64/R/library/furrr/R/furrr.rdb
/usr/lib64/R/library/furrr/R/furrr.rdx
/usr/lib64/R/library/furrr/help/AnIndex
/usr/lib64/R/library/furrr/help/aliases.rds
/usr/lib64/R/library/furrr/help/furrr.rdb
/usr/lib64/R/library/furrr/help/furrr.rdx
/usr/lib64/R/library/furrr/help/paths.rds
/usr/lib64/R/library/furrr/html/00Index.html
/usr/lib64/R/library/furrr/html/R.css
/usr/lib64/R/library/furrr/tests/testthat.R
/usr/lib64/R/library/furrr/tests/testthat/helper-test-setup.R
/usr/lib64/R/library/furrr/tests/testthat/test-future-options.R
/usr/lib64/R/library/furrr/tests/testthat/test-map.R
/usr/lib64/R/library/furrr/tests/testthat/test-map2.R
/usr/lib64/R/library/furrr/tests/testthat/test-pmap.R
/usr/lib64/R/library/furrr/tests/testthat/test-progress.R
