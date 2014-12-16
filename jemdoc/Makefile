DOCS=index blate cal_band calopoly edi ee100_sum_12 ee192 egg_mobile man mpf network_rehab pie rel_nonrel tailbot1 tailbot2 target_shoot jpl_cssr

HDOCS=$(addsuffix .html, $(DOCS))
PHDOCS=$(addprefix ../, $(HDOCS))

.PHONY : docs
docs : $(PHDOCS)

../%.html : %.jemdoc MENU
	jemdoc -o $@ $<

.PHONY : clean
clean :
	-rm -f html/*.html