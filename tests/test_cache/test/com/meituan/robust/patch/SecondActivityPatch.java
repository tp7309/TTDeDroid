/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  android.content.Context
 *  android.os.Bundle
 *  android.os.Handler
 *  android.support.v7.app.u
 *  android.util.Log
 *  android.view.View
 *  android.view.View$OnClickListener
 *  android.widget.ArrayAdapter
 *  android.widget.ListAdapter
 *  android.widget.ListView
 *  android.widget.TextView
 *  com.meituan.robust.patch.RobustModify
 *  com.meituan.robust.utils.EnhancedRobustUtils
 *  com.meituan.sample.SecondActivity
 *  com.meituan.sample.j
 *  com.meituan.sample.robusttest.a
 *  com.meituan.sample.robusttest.c
 *  com.meituan.sample.robusttest.k
 *  com.meituan.sample.robusttest.o
 *  com.meituan.sample.robusttest.other.a
 *  com.meituan.sample.robusttest.p
 */
package com.meituan.robust.patch;

import android.content.Context;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.u;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.TextView;
import com.meituan.robust.patch.RobustModify;
import com.meituan.robust.patch.SecondActivityPatchRobustAssist;
import com.meituan.robust.utils.EnhancedRobustUtils;
import com.meituan.sample.SecondActivity;
import com.meituan.sample.j;
import com.meituan.sample.robusttest.c;
import com.meituan.sample.robusttest.k;
import com.meituan.sample.robusttest.o;
import com.meituan.sample.robusttest.other.a;
import com.meituan.sample.robusttest.p;
import java.io.PrintStream;

public class SecondActivityPatch {
    SecondActivity originClass;

    public SecondActivityPatch(Object object) {
        this.originClass = (SecondActivity)object;
    }

    /*
     * Enabled aggressive block sorting
     */
    private /* synthetic */ void lambda$onCreate$0(View object) {
        void var1_3;
        k k2;
        void var1_6;
        EnhancedRobustUtils.invokeReflectStaticMethod((String)"modify", RobustModify.class, (Object[])this.getRealParameter(new Object[0]), null);
        if (this instanceof SecondActivityPatch) {
            SecondActivity secondActivity = this.originClass;
        } else {
            SecondActivityPatch secondActivityPatch = this;
        }
        k k3 = k2 = (k)EnhancedRobustUtils.getFieldValue((String)"s", (Object)var1_3, SecondActivity.class);
        if (k2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)k2).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"a", (Object)var1_6, (Object[])this.getRealParameter(new Object[]{"asdasd"}), (Class[])new Class[]{String.class}, k.class);
        o o2 = SecondActivity.r;
        k2 = (p)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.robusttest.p", (Object[])new Object[0], null);
        String string = (String)EnhancedRobustUtils.invokeReflectMethod((String)"a", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{o2, k2, new Long(1L)}), (Class[])new Class[]{o.class, p.class, Long.TYPE}, SecondActivity.class);
        ((Integer)EnhancedRobustUtils.invokeReflectStaticMethod((String)"d", Log.class, (Object[])this.getRealParameter(new Object[]{"robust", " onclick  in Listener"}), (Class[])new Class[]{String.class, String.class})).intValue();
    }

    public static void staticRobustonCreate(SecondActivityPatch secondActivityPatch, SecondActivity secondActivity, Bundle bundle) {
        SecondActivityPatchRobustAssist.staticRobustonCreate(secondActivityPatch, secondActivity, bundle);
    }

    public void RobustPubliclambda$onCreate$0(View view) {
        this.lambda$onCreate$0(view);
    }

    /*
     * Enabled aggressive block sorting
     */
    public Object[] getRealParameter(Object[] arrobject) {
        Object[] arrobject2 = arrobject;
        if (arrobject == null) return arrobject2;
        if (arrobject.length < 1) {
            return arrobject;
        }
        arrobject2 = new Object[arrobject.length];
        int n2 = 0;
        while (n2 < arrobject.length) {
            arrobject2[n2] = arrobject[n2] == this ? this.originClass : arrobject[n2];
            ++n2;
        }
        return arrobject2;
    }

    /*
     * Enabled aggressive block sorting
     */
    public String getTextInfo(Object[] object) {
        void var1_11;
        void var1_14;
        void var3_29;
        void var2_20;
        StringBuilder stringBuilder;
        k k2;
        void var2_17;
        void var1_8;
        StringBuilder stringBuilder2;
        void var1_5;
        void var3_26;
        k k3 = (k)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.robusttest.k", (Object[])new Object[0], null);
        if (k3 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)k3).originClass;
        } else {
            k k4 = k3;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"c", (Object)var3_26, (Object[])this.getRealParameter(new Object[]{"mivazhang"}), (Class[])new Class[]{String.class}, k.class);
        k k5 = k3;
        if (k3 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)k3).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"b", (Object)var3_29, (Object[])this.getRealParameter(new Object[]{"  AutoPatch"}), (Class[])new Class[]{String.class}, k.class);
        if (this instanceof SecondActivityPatch) {
            SecondActivity secondActivity = this.originClass;
        } else {
            SecondActivityPatch secondActivityPatch = this;
        }
        k k6 = k2 = (k)EnhancedRobustUtils.getFieldValue((String)"s", (Object)var2_17, SecondActivity.class);
        if (k2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)k2).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"c", (Object)var2_20, (Object[])this.getRealParameter(new Object[]{" I am Patch"}), (Class[])new Class[]{String.class}, k.class);
        c c2 = (c)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.robusttest.c", (Object[])new Object[0], null);
        String[] arrstring = (String[])EnhancedRobustUtils.invokeReflectMethod((String)"b", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{object}), (Class[])new Class[]{Object[].class}, SecondActivity.class);
        StringBuilder stringBuilder3 = stringBuilder2 = (StringBuilder)EnhancedRobustUtils.invokeReflectConstruct((String)"java.lang.StringBuilder", (Object[])new Object[0], null);
        if (stringBuilder2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)stringBuilder2).originClass;
        }
        StringBuilder stringBuilder4 = (StringBuilder)EnhancedRobustUtils.invokeReflectMethod((String)"append", (Object)var1_5, (Object[])this.getRealParameter(new Object[]{"error Fix "}), (Class[])new Class[]{String.class}, StringBuilder.class);
        c c3 = c2;
        if (c2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)c2).originClass;
        }
        String string = (String)EnhancedRobustUtils.invokeReflectMethod((String)"a", (Object)var1_8, (Object[])new Object[0], null, com.meituan.sample.robusttest.a.class);
        StringBuilder stringBuilder5 = stringBuilder4;
        if (stringBuilder4 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)stringBuilder4).originClass;
        }
        StringBuilder stringBuilder6 = stringBuilder = (StringBuilder)EnhancedRobustUtils.invokeReflectMethod((String)"append", (Object)var1_11, (Object[])this.getRealParameter(new Object[]{string}), (Class[])new Class[]{String.class}, StringBuilder.class);
        if (stringBuilder == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)stringBuilder).originClass;
        }
        return (String)EnhancedRobustUtils.invokeReflectMethod((String)"toString", (Object)var1_14, (Object[])new Object[0], null, StringBuilder.class);
    }

    /*
     * Enabled aggressive block sorting
     */
    protected void onCreate(Bundle object) {
        void var1_25;
        void var1_22;
        void var1_28;
        void var1_20;
        void var1_47;
        void var1_41;
        void var1_44;
        void var1_38;
        void var1_10;
        void var1_35;
        void var1_14;
        void var1_31;
        void var1_17;
        void var1_12;
        void var1_6;
        void var1_4;
        void var1_50;
        SecondActivityPatch.staticRobustonCreate(this, this.originClass, (Bundle)object);
        Object object2 = System.out;
        Object object3 = (String)EnhancedRobustUtils.invokeReflectMethod((String)"i", (Object)this.originClass, (Object[])new Object[0], null, SecondActivity.class);
        PrintStream printStream = object2;
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"println", (Object)var1_4, (Object[])this.getRealParameter(new Object[]{object3}), (Class[])new Class[]{String.class}, PrintStream.class);
        EnhancedRobustUtils.invokeReflectMethod((String)"setContentView", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{new Integer(2130968603)}), (Class[])new Class[]{Integer.TYPE}, u.class);
        object2 = (ListView)((View)EnhancedRobustUtils.invokeReflectMethod((String)"findViewById", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{new Integer(2131492980)}), (Class[])new Class[]{Integer.TYPE}, u.class));
        if (this instanceof SecondActivityPatch) {
            SecondActivity secondActivity = this.originClass;
        } else {
            SecondActivityPatch secondActivityPatch = this;
        }
        EnhancedRobustUtils.setFieldValue((String)"t", (Object)var1_6, (Object)object2, SecondActivity.class);
        TextView textView = (TextView)((View)EnhancedRobustUtils.invokeReflectMethod((String)"findViewById", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{new Integer(2131492981)}), (Class[])new Class[]{Integer.TYPE}, u.class));
        object3 = (View.OnClickListener)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.g", (Object[])this.getRealParameter(new Object[]{this}), (Class[])new Class[]{SecondActivity.class});
        object2 = textView == this ? ((SecondActivityPatch)textView).originClass : textView;
        EnhancedRobustUtils.invokeReflectMethod((String)"setOnClickListener", (Object)object2, (Object[])this.getRealParameter(new Object[]{object3}), (Class[])new Class[]{View.OnClickListener.class}, View.class);
        object2 = (String)EnhancedRobustUtils.getStaticFieldValue((String)"p", SecondActivity.class);
        object3 = (String)EnhancedRobustUtils.invokeReflectMethod((String)"a", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{new Object[]{object2}}), (Class[])new Class[]{Object[].class}, SecondActivity.class);
        object2 = textView;
        if (textView == this) {
            object2 = ((SecondActivityPatch)textView).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"setText", (Object)object2, (Object[])this.getRealParameter(new Object[]{object3}), (Class[])new Class[]{CharSequence.class}, TextView.class);
        object2 = (Handler)EnhancedRobustUtils.invokeReflectConstruct((String)"android.os.Handler", (Object[])new Object[0], null);
        object3 = (j)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.j", (Object[])this.getRealParameter(new Object[]{this, this}), (Class[])new Class[]{SecondActivity.class, SecondActivity.class});
        Object object4 = object2;
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        ((Boolean)EnhancedRobustUtils.invokeReflectMethod((String)"postDelayed", (Object)var1_10, (Object[])this.getRealParameter(new Object[]{object3, new Long(1100L)}), (Class[])new Class[]{Runnable.class, Long.TYPE}, Handler.class)).booleanValue();
        if (this instanceof SecondActivityPatch) {
            SecondActivity secondActivity = this.originClass;
        } else {
            SecondActivityPatch secondActivityPatch = this;
        }
        object2 = (a)EnhancedRobustUtils.getFieldValue((String)"q", (Object)var1_12, SecondActivity.class);
        if (this instanceof SecondActivityPatch) {
            SecondActivity secondActivity = this.originClass;
        } else {
            SecondActivityPatch secondActivityPatch = this;
        }
        object3 = (String)EnhancedRobustUtils.getFieldValue((String)"o", (Object)var1_14, SecondActivity.class);
        Object object5 = object2;
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        ((Integer)EnhancedRobustUtils.invokeReflectStaticMethod((String)"d", Log.class, (Object[])this.getRealParameter(new Object[]{"robust", (String)EnhancedRobustUtils.invokeReflectMethod((String)"a", (Object)var1_17, (Object[])this.getRealParameter(new Object[]{new Integer(1), object3}), (Class[])new Class[]{Integer.TYPE, String.class}, a.class)}), (Class[])new Class[]{String.class, String.class})).intValue();
        ((Integer)EnhancedRobustUtils.invokeReflectStaticMethod((String)"d", Log.class, (Object[])this.getRealParameter(new Object[]{"robust", (String)EnhancedRobustUtils.invokeReflectMethod((String)"getString", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{new Integer(2131099681)}), (Class[])new Class[]{Integer.TYPE}, Context.class)}), (Class[])new Class[]{String.class, String.class})).intValue();
        Object object6 = object2 = (StringBuilder)EnhancedRobustUtils.invokeReflectConstruct((String)"java.lang.StringBuilder", (Object[])new Object[0], null);
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        object2 = (StringBuilder)EnhancedRobustUtils.invokeReflectMethod((String)"append", (Object)var1_20, (Object[])this.getRealParameter(new Object[]{"getValue is   "}), (Class[])new Class[]{String.class}, StringBuilder.class);
        if (this instanceof SecondActivityPatch) {
            SecondActivity secondActivity = this.originClass;
        } else {
            SecondActivityPatch secondActivityPatch = this;
        }
        object3 = EnhancedRobustUtils.invokeReflectStaticMethod((String)"b", SecondActivity.class, (Object[])this.getRealParameter(new Object[]{"a", (a)EnhancedRobustUtils.getFieldValue((String)"q", (Object)var1_22, SecondActivity.class)}), (Class[])new Class[]{String.class, Object.class});
        Object object7 = object2;
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        Object object8 = object2 = (StringBuilder)EnhancedRobustUtils.invokeReflectMethod((String)"append", (Object)var1_25, (Object[])this.getRealParameter(new Object[]{object3}), (Class[])new Class[]{Object.class}, StringBuilder.class);
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        ((Integer)EnhancedRobustUtils.invokeReflectStaticMethod((String)"d", Log.class, (Object[])this.getRealParameter(new Object[]{"robust", (String)EnhancedRobustUtils.invokeReflectMethod((String)"toString", (Object)var1_28, (Object[])new Object[0], null, StringBuilder.class)}), (Class[])new Class[]{String.class, String.class})).intValue();
        Object object9 = object2 = (StringBuilder)EnhancedRobustUtils.invokeReflectConstruct((String)"java.lang.StringBuilder", (Object[])new Object[0], null);
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        object2 = (StringBuilder)EnhancedRobustUtils.invokeReflectMethod((String)"append", (Object)var1_31, (Object[])this.getRealParameter(new Object[]{"=========="}), (Class[])new Class[]{String.class}, StringBuilder.class);
        object3 = SecondActivity.r;
        p p2 = (p)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.robusttest.p", (Object[])new Object[0], null);
        object3 = (String)EnhancedRobustUtils.invokeReflectMethod((String)"a", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{object3, p2, new Long(1L)}), (Class[])new Class[]{o.class, p.class, Long.TYPE}, SecondActivity.class);
        Object object10 = object2;
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        Object object11 = object2 = (StringBuilder)EnhancedRobustUtils.invokeReflectMethod((String)"append", (Object)var1_35, (Object[])this.getRealParameter(new Object[]{object3}), (Class[])new Class[]{String.class}, StringBuilder.class);
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        Object object12 = object2 = (StringBuilder)EnhancedRobustUtils.invokeReflectMethod((String)"append", (Object)var1_38, (Object[])this.getRealParameter(new Object[]{"============="}), (Class[])new Class[]{String.class}, StringBuilder.class);
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        ((Integer)EnhancedRobustUtils.invokeReflectStaticMethod((String)"d", Log.class, (Object[])this.getRealParameter(new Object[]{"robust", (String)EnhancedRobustUtils.invokeReflectMethod((String)"toString", (Object)var1_41, (Object[])new Object[0], null, StringBuilder.class)}), (Class[])new Class[]{String.class, String.class})).intValue();
        Bundle bundle = new Bundle();
        bundle.putInt("asd", 1);
        bundle.getFloat("asd");
        if (this instanceof SecondActivityPatch) {
            SecondActivity secondActivity = this.originClass;
        } else {
            SecondActivityPatch secondActivityPatch = this;
        }
        String[] arrstring = (String[])EnhancedRobustUtils.getFieldValue((String)"u", (Object)var1_44, SecondActivity.class);
        object3 = (ArrayAdapter)EnhancedRobustUtils.invokeReflectConstruct((String)"android.widget.ArrayAdapter", (Object[])this.getRealParameter(new Object[]{this, new Integer(17367046), arrstring}), (Class[])new Class[]{Context.class, Integer.TYPE, Object[].class});
        if (this instanceof SecondActivityPatch) {
            SecondActivity secondActivity = this.originClass;
        } else {
            SecondActivityPatch secondActivityPatch = this;
        }
        Object object13 = object2 = (ListView)EnhancedRobustUtils.getFieldValue((String)"t", (Object)var1_47, SecondActivity.class);
        if (object2 == this) {
            SecondActivity secondActivity = ((SecondActivityPatch)object2).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"setAdapter", (Object)var1_50, (Object[])this.getRealParameter(new Object[]{object3}), (Class[])new Class[]{ListAdapter.class}, ListView.class);
    }
}

