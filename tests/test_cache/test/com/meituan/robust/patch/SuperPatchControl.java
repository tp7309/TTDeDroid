/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  com.meituan.robust.ChangeQuickRedirect
 *  com.meituan.sample.robusttest.p
 */
package com.meituan.robust.patch;

import com.meituan.robust.ChangeQuickRedirect;
import com.meituan.robust.patch.SuperPatch;
import com.meituan.sample.robusttest.p;
import java.util.Map;
import java.util.WeakHashMap;

public class SuperPatchControl
implements ChangeQuickRedirect {
    public static final String MATCH_ALL_PARAMETER = "(\\w*\\.)*\\w*";
    private static final Map<Object, Object> keyToValueRelation = new WeakHashMap<Object, Object>();

    /*
     * Enabled aggressive block sorting
     * Enabled unnecessary exception pruning
     * Enabled aggressive exception aggregation
     */
    public Object accessDispatch(String string, Object[] arrobject) {
        try {
            SuperPatch superPatch;
            if (string.split(":")[2].equals("false")) {
                if (keyToValueRelation.get(arrobject[arrobject.length - 1]) == null) {
                    superPatch = new SuperPatch(arrobject[arrobject.length - 1]);
                    keyToValueRelation.put(arrobject[arrobject.length - 1], superPatch);
                } else {
                    superPatch = (SuperPatch)keyToValueRelation.get(arrobject[arrobject.length - 1]);
                }
            } else {
                superPatch = new SuperPatch(null);
            }
            if (!"75".equals(string.split(":")[3])) return null;
            return superPatch.getText1((Integer)arrobject[0], (Long)arrobject[1], (Integer)arrobject[2]);
        }
        catch (Throwable throwable) {
            throwable.printStackTrace();
        }
        return null;
    }

    public Object getRealParameter(Object object) {
        Object object2 = object;
        if (object instanceof p) {
            object2 = new SuperPatch(object);
        }
        return object2;
    }

    public boolean isSupport(String string, Object[] arrobject) {
        return "75:".contains(string.split(":")[3]);
    }
}

