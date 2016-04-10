#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R6
Version  : 2.1.2
Release  : 21
URL      : http://cran.r-project.org/src/contrib/R6_2.1.2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/R6_2.1.2.tar.gz
Summary  : Classes with Reference Semantics
Group    : Development/Tools
License  : MIT
Requires: R-pryr
Requires: R-microbenchmark
BuildRequires : R-knitr
BuildRequires : R-microbenchmark
BuildRequires : R-pryr
BuildRequires : clr-R-helpers

%description
The tests in this directory are somewhat invasive, so they must be run by hand,
and therefore are kept separate from the automated tests.

%prep
%setup -q -c -n R6

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library R6
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library R6


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R6/DESCRIPTION
/usr/lib64/R/library/R6/INDEX
/usr/lib64/R/library/R6/LICENSE
/usr/lib64/R/library/R6/Meta/Rd.rds
/usr/lib64/R/library/R6/Meta/hsearch.rds
/usr/lib64/R/library/R6/Meta/links.rds
/usr/lib64/R/library/R6/Meta/nsInfo.rds
/usr/lib64/R/library/R6/Meta/package.rds
/usr/lib64/R/library/R6/Meta/vignette.rds
/usr/lib64/R/library/R6/NAMESPACE
/usr/lib64/R/library/R6/NEWS
/usr/lib64/R/library/R6/R/R6
/usr/lib64/R/library/R6/R/R6.rdb
/usr/lib64/R/library/R6/R/R6.rdx
/usr/lib64/R/library/R6/doc/Debugging.R
/usr/lib64/R/library/R6/doc/Debugging.Rmd
/usr/lib64/R/library/R6/doc/Debugging.html
/usr/lib64/R/library/R6/doc/Introduction.R
/usr/lib64/R/library/R6/doc/Introduction.Rmd
/usr/lib64/R/library/R6/doc/Introduction.html
/usr/lib64/R/library/R6/doc/Performance.R
/usr/lib64/R/library/R6/doc/Performance.Rmd
/usr/lib64/R/library/R6/doc/Performance.html
/usr/lib64/R/library/R6/doc/Portable.R
/usr/lib64/R/library/R6/doc/Portable.Rmd
/usr/lib64/R/library/R6/doc/Portable.html
/usr/lib64/R/library/R6/doc/index.html
/usr/lib64/R/library/R6/help/AnIndex
/usr/lib64/R/library/R6/help/R6.rdb
/usr/lib64/R/library/R6/help/R6.rdx
/usr/lib64/R/library/R6/help/aliases.rds
/usr/lib64/R/library/R6/help/paths.rds
/usr/lib64/R/library/R6/html/00Index.html
/usr/lib64/R/library/R6/html/R.css