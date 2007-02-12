%include	/usr/lib/rpm/macros.perl
Summary:	Cover generator
Summary(pl.UTF-8):   Generator okładek
Name:		disc-cover
Version:	1.5.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.vanhemert.co.uk/files/%{name}-%{version}.tar.gz
# Source0-md5:	4d8cf0e644a9b311f7e6ed44944b9033
URL:		http://www.vanhemert.co.uk/disc-cover.html
Requires:	tetex-dvips
Requires:	tetex-format-latex
Requires:	ImageMagick
Requires:	perl-Audio-CD
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
disc-cover provides an easy way to produce covers for audio cds. It
scans audio cds and uses information from the freedb database to build
a back and front cover for the cd. The cover is output is in Latex,
Dvi, Pdf or Postscript. This little gadget lets you produce covers
without typing in all the information yourself.

%description -l pl.UTF-8
disc-cover udostępnia łatwy sposób produkcji okładek na płyty z
muzyką. Skanuje płytę i używa informacji z bazy danych freedb, by
złożyć przednią i tylną okładkę. Formaty wyjściowe to latex, dvi, pdf,
postscript. Dzięki temu małemu gadżetowi możesz robić okładki nie
wpisując żadnych informacji.

%prep
%setup -q

%build
./disc-cover -H > README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/templates}

install disc-cover $RPM_BUILD_ROOT%{_bindir}
install templates/* $RPM_BUILD_ROOT%{_datadir}/%{name}/templates

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG TODO README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
