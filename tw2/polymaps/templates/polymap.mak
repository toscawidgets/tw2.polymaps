<%namespace name="tw" module="tw2.core.mako_util"/>
<div>
<div ${tw.attrs(attrs=w.attrs)}>
<div id="${w.attrs['id']}:target"></div>
</div>
<script type="text/javascript">
	var map = setupPolymap(${w.j('attrs')});
	map = setupPolymapControls(map,
	            ${w.j('arrow')}, ${w.j('compass')}, ${w.j('dblclick')},
				${w.j('drag')}, ${w.j('grid')}, ${w.j('hash')},
				${w.j('interact')}, ${w.j('wheel')}
	);
	% if hasattr(w, 'interval'):
	map = setupPolymapPollingData(map, ${w.j('data_url')}, ${w.j('interval')});
	% else:
	map = setupPolymapData(map, ${w.j('data_url')});
	% endif
</script>
</div>
