%include	/usr/lib/rpm/macros.perl
Summary:	Cover generator
Summary(pl):	Generator ok³adek
Name:		disc-cover
Version:	1.5.2
Release:	1
License:	GPL
Group:		Applications
# Source0-md5:	a7b6a95efa46e8eacde536be16eaa253
Source0:	http://home.wanadoo.nl/jano/files/%{name}-%{version}.tar.gz
URL:		http://home.wanadoo.nl/jano/disc-cover.html
Requires:	tetex-dvips
Requires:	tetex-format-latex
Requires:	ImageMagick
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Audio-CD
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
disc-cover provides an easy way to produce covers for audio cds. It
scans audio cds and uses information from the freedb database to build
a back and front cover for the cd. The cover is output is in Latex,
Dvi, Pdf or Postscript. This little gadget lets you produce covers
without typing in all the information yourself.

%description -l pl
disc-cover udostêpnia ³atwy sposób produkcji ok³adek na p³yty z
muzyk±. Skanuje p³ytê i u¿ywa informacji z bazy danych freedb, by
z³o¿yæ przedni± i tyln± ok³adkê. Formaty wyj¶ciowe to latex, dvi, pdf,
postscript. Dziêki temu ma³emu gad¿etowi mo¿esz robiæ ok³adki nie
wpisuj±c ¿adnych informacji.

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
