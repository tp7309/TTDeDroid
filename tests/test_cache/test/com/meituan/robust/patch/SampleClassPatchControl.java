/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  com.meituan.robust.ChangeQuickRedirect
 *  com.meituan.sample.robusttest.l
 */
package com.meituan.robust.patch;

import com.meituan.robust.ChangeQuickRedirect;
import com.meituan.robust.patch.SampleClassPatch;
import com.meituan.sample.robusttest.l;
import java.util.Map;
import java.util.WeakHashMap;

public class SampleClassPatchControl
implements ChangeQuickRedirect {
    public static final String MATCH_ALL_PARAMETER = "(\\w*\\.)*\\w*";
    private static final Map<Object, Object> keyToValueRelation = new WeakHashMap<Object, Object>();

    /*
     * Enabled aggressive block sorting
     * Enabled unnecessary exception pruning
     * Enabled aggressive exception aggregation
     */
    public Object accessDispatch(String object, Object[] arrobject) {
        try {
            SampleClassPatch sampleClassPatch;
            if (object.split(":")[2].equals("false")) {
                if (keyToValueRelation.get(arrobject[arrobject.length - 1]) == null) {
                    sampleClassPatch = new SampleClassPatch(arrobject[arrobject.length - 1]);
                    keyToValueRelation.put(arrobject[arrobject.length - 1], sampleClassPatch);
                } else {
                    sampleClassPatch = (SampleClassPatch)keyToValueRelation.get(arrobject[arrobject.length - 1]);
                }
            } else {
                sampleClassPatch = new SampleClassPatch(null);
            }
            if (!"66".equals(object.split(":")[3])) return null;
            return sampleClassPatch.multiple((Integer)arrobject[0]);
        }
        catch (Throwable throwable) {
            throwable.printStackTrace();
        }
        return null;
    }

    public Object getRealParameter(Object object) {
        Object object2 = object;
        if (object instanceof l) {
            object2 = new SampleClassPatch(object);
        }
        return object2;
    }

    public boolean isSupport(String string, Object[] arrobject) {
        return "66:".contains(string.split(":")[3]);
    }
}

