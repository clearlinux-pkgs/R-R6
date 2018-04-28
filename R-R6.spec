#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R6
Version  : 2.2.2
Release  : 56
URL      : https://cran.r-project.org/src/contrib/R6_2.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/R6_2.2.2.tar.gz
Summary  : Classes with Reference Semantics
Group    : Development/Tools
License  : MIT
BuildRequires : R-formatR
BuildRequires : R-ggplot2
BuildRequires : R-knitr
BuildRequires : R-microbenchmark
BuildRequires : R-pryr
BuildRequires : R-scales
BuildRequires : clr-R-helpers

%description
semantics, similar to R's built-in reference classes. Compared to reference
    classes, R6 classes are simpler and lighter-weight, and they are not built
    on S4 classes so they do not require the methods package. These classes
    allow public and private members, and they support inheritance, even when
    the classes are defined in different packages.

%prep
%setup -q -c -n R6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524478289

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1524478289
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R6
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R6
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R6
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library R6|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R6/DESCRIPTION
/usr/lib64/R/library/R6/INDEX
/usr/lib64/R/library/R6/LICENSE
/usr/lib64/R/library/R6/Meta/Rd.rds
/usr/lib64/R/library/R6/Meta/features.rds
/usr/lib64/R/library/R6/Meta/hsearch.rds
/usr/lib64/R/library/R6/Meta/links.rds
/usr/lib64/R/library/R6/Meta/nsInfo.rds
/usr/lib64/R/library/R6/Meta/package.rds
/usr/lib64/R/library/R6/Meta/vignette.rds
/usr/lib64/R/library/R6/NAMESPACE
/usr/lib64/R/library/R6/NEWS.md
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
