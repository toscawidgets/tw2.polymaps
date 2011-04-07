<%namespace name="tw" module="tw2.core.mako_util"/>
<div>
<div ${tw.attrs(attrs=w.attrs)}>
<div id="${w.attrs['id']}:target"></div>
</div>
<script type="text/javascript">
	setupPolymap(${w.js_arguments()});
</script>
</div>
