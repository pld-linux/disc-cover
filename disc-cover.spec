%include	/usr/lib/rpm/macros.perl
Summary:	Cover generator
Summary(pl):	Generator ok�adek
Name:		disc-cover
Version:	1.4.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://home.wanadoo.nl/jano/files/%{name}-%{version}.tar.gz
URL:		http://home.wanadoo.nl/jano/disc-cover.html
Requires:	tetex-dvips
Requires:	tetex-latex
Requires:	ImageMagick
BuildRequires:	perl >= 5.6
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
disc-cover udost�pnia �atwy spos�b produkcji ok�adek na p�yty z
muzyk�. Skanuje p�yt� i u�ywa informacji z bazy danych freedb, by
z�o�y� przedni� i tyln� ok�adk�. Formaty wyj�ciowe to latex, dvi, pdf,
postscript. Dzi�ki temu ma�emu gad�etowi mo�esz robi� ok�adki nie
wpisuj�c �adnych informacji.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install disc-cover $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG TODO
%attr(755,root,root) %{_bindir}/*