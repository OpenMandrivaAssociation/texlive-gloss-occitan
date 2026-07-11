%global tl_name gloss-occitan
%global tl_revision 52593

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Polyglossia support for Occitan
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gloss-occitan
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss-occitan.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss-occitan.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss-occitan.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Occitan language description file for polyglossia

