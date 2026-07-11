%global tl_name callout-itembox
%global tl_revision 79339

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A LaTeX package for colored callout item/numbered text boxes with a tinted
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/callout-itembox
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/callout-itembox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/callout-itembox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A small LaTeX package for colored callout item/numbered boxes with a
tinted background, a colored side bar with circular/numbered marker.
Each box can show a bold colored heading plus body text, or body text
only.

