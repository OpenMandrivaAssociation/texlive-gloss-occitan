Name:		texlive-gloss-occitan
Version:	52593
Release:	2
Summary:	Polyglossia support for Occitan
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gloss-occitan
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss-occitan.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss-occitan.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss-occitan.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Occitan language description file for polyglossia

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gloss-occitan
%doc %{_texmfdistdir}/doc/latex/gloss-occitan

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
